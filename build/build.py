#!/usr/bin/env python3
"""把 site_data.json 的 14 组对比数据注入 template.html，生成 public/index.html。
每组用 ffprobe 判定横/竖版，供页面自适应容器比例。
用法: python3 build/build.py"""
import json, pathlib, subprocess

base = pathlib.Path(__file__).resolve().parent
videos = base.parent / 'public' / 'videos'
data = json.load(open(base / 'site_data.json', encoding='utf-8'))

def orient(fname):
    """返回 'portrait' 或 'landscape'（读不到时默认 landscape）。"""
    try:
        out = subprocess.check_output(
            ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
             '-show_entries', 'stream=width,height', '-of', 'csv=p=0',
             str(videos / fname)], text=True).strip()
        w, h = (float(x) for x in out.split(','))
        return 'portrait' if w / h < 1 else 'landscape'
    except Exception:
        return 'landscape'

slim = [{'id': d['id'], 'prompt': d['prompt'], 'vidu': d['vidu'], 'sd': d['sd'],
         'orient': orient(d['vidu'])} for d in data]

tpl = open(base / 'template.html', encoding='utf-8').read()
out = tpl.replace('/*__DATA__*/ []', json.dumps(slim, ensure_ascii=False))

target = base.parent / 'public' / 'index.html'
target.parent.mkdir(parents=True, exist_ok=True)
open(target, 'w', encoding='utf-8').write(out)
np = sum(1 for s in slim if s['orient'] == 'portrait')
print(f'✓ 生成 {target} （{len(slim)} 组：{np} 竖版 / {len(slim)-np} 横版，{len(out)} 字节）')

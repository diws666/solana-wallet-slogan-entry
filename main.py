LINE = "Solana in your pocket, awake around the clock: it signs, swaps, and saves while you just live your life."  # verified: 104 chars, 19 words

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

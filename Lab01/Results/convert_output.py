import json
import pandas as pd
import os
import re
import sys

def extract_page_number(filename):
    base = os.path.basename(filename)
    name, ext = os.path.splitext(base)
    match = re.search(r'-(\d+)$', name)
    if match:
        return match.group(1)
    return name

def main():
    possible_paths = ['Label.txt', 'Results/Label.txt']
    label_file = None

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            label_file = sys.argv[1]
        else:
            print(f"Error: Specified file {sys.argv[1]} not found.")
            return
    else:
        for path in possible_paths:
            if os.path.exists(path):
                label_file = path
                break

    if not label_file:
        print(f"Error: Label.txt not found in {possible_paths}.")
        return

    print(f"Reading from {label_file}")
    output_file = 'output.xlsx'

    data = []

    with open(label_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split('\t', 1)
            if len(parts) != 2:
                print(f"Skipping invalid line: {line[:50]}...")
                continue

            image_path, json_str = parts
            page_id = extract_page_number(image_path)

            try:
                boxes = json.loads(json_str)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for {image_path}: {e}")
                continue

            for box in boxes:
                text = box.get('transcription', '')
                points = box.get('points', [])

                points_str = str(points)

                data.append({
                    'ID': page_id,
                    'Image box': points_str,
                    'Text': text
                })

    df = pd.DataFrame(data)

    df = df[['ID', 'Image box', 'Text']]

    df.to_excel(output_file, index=False)
    print(f"Successfully created {output_file} with {len(df)} rows.")

if __name__ == "__main__":
    main()
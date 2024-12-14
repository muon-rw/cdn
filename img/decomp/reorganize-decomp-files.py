import os
import shutil
from collections import defaultdict

def organize_decomp_files(base_path):
    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)

        if not os.path.isdir(category_path) or category.startswith('.'):
            continue
]
        prefix_groups = defaultdict(list)

        for filename in os.listdir(category_path):
            if not filename.endswith('.png'):
                continue

            prefix = filename.split('_')[0]
            prefix_groups[prefix].append(filename)

        if len(prefix_groups) > 1:
            print(f"\nProcessing {category}:")
            print(f"Found {len(prefix_groups)} different types: {', '.join(prefix_groups.keys())}")

            for prefix, files in prefix_groups.items():
                subdir = os.path.join(category_path, prefix)

                if not os.path.exists(subdir):
                    os.makedirs(subdir)
                    print(f"Created directory: {subdir}")

                for file in files:
                    src = os.path.join(category_path, file)
                    dst = os.path.join(subdir, file)
                    shutil.move(src, dst)
                print(f"Moved {len(files)} files to {prefix}/")

if __name__ == "__main__":
    base_path = "FILL_ME"

    if not os.path.exists(base_path):
        print(f"Error: Path {base_path} does not exist!")
    else:
        organize_decomp_files(base_path)
        print("\nOrganization complete!")
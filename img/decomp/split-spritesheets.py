from PIL import Image
import os
import sys

def split_spritesheet(spritesheet_path, output_dir, sprite_width=16, sprite_height=16):
    base_name = os.path.splitext(os.path.basename(spritesheet_path))[0]

    if not os.path.exists(spritesheet_path):
        print(f"Error: File '{spritesheet_path}' not found!")
        return False

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        sheet = Image.open(spritesheet_path).convert('RGBA')
        width, height = sheet.size

        if width % sprite_width != 0 or height % sprite_height != 0:
            print(f"Warning: Spritesheet dimensions ({width}x{height}) are not perfectly divisible by sprite size ({sprite_width}x{sprite_height})")

        rows = height // sprite_height
        cols = width // sprite_width

        count = 0
        for row in range(rows):
            for col in range(cols):
                left = col * sprite_width
                upper = row * sprite_height
                right = left + sprite_width
                lower = upper + sprite_height

                sprite = sheet.crop((left, upper, right, lower))

                if max(sprite.getchannel('A').getextrema()) == 0:
                    continue

                output_path = os.path.join(output_dir, f'{base_name}_{row:03d}_{col:03d}.png')
                sprite.save(output_path)
                count += 1

        print(f"Successfully extracted {count} sprites to {output_dir}")
        return True

    except Exception as e:
        print(f"Error processing spritesheet: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_spritesheet.py <spritesheet_path> [output_dir] [sprite_width] [sprite_height]")
        sys.exit(1)

    spritesheet_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output_sprites"
    sprite_width = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    sprite_height = int(sys.argv[4]) if len(sys.argv) > 4 else 16

    split_spritesheet(spritesheet_path, output_dir, sprite_width, sprite_height)
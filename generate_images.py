from PIL import Image, ImageDraw, ImageFont
import os


def ensure_directory_exists(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def create_centered_text_image(width: int, height: int, background_rgb: tuple[int, int, int], text: str, output_path: str) -> None:
    image = Image.new("RGB", (width, height), background_rgb)
    drawer = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except Exception:
        font = ImageFont.load_default()

    # Compute text size; Pillow versions differ on API availability
    try:
        left, top, right, bottom = drawer.textbbox((0, 0), text, font=font)
        text_width, text_height = right - left, bottom - top
    except Exception:
        text_width, text_height = drawer.textsize(text, font=font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2
    drawer.text((x, y), text, fill=(255, 255, 255), font=font)
    image.save(output_path, quality=85)


def main() -> None:
    images_dir = os.path.join("static", "images")
    ensure_directory_exists(images_dir)

    book_backgrounds = {
        1: (66, 135, 245),    # blue
        2: (76, 175, 80),     # green
        3: (244, 67, 54),     # red
    }

    for book_id, bg in book_backgrounds.items():
        filename = os.path.join(images_dir, f"book{book_id}.jpg")
        create_centered_text_image(600, 800, bg, f"Book {book_id}", filename)
        print(f"Created {filename}")


if __name__ == "__main__":
    main()



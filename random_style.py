from gradio_client import Client
from pathlib import Path
import random
import shutil

from helper import generate, get_all_styles, set_parameters


def main():
    positive_prompt = 'Pomsky'
    negative_prompt = ''
    seed = random.randint(0, 2 ** 32 - 1)

    cwd = Path.cwd()
    base_path = cwd / 'images' / 'random_style'
    base_path.mkdir(exist_ok=True, parents=True)

    client = Client('http://localhost:7865', serialize=False)
    styles = get_all_styles(client)
    style = random.choice(styles)
    print(f'Generating image with style: {style}')
    set_parameters(client, positive_prompt=positive_prompt, negative_prompt=negative_prompt, seed=seed, style=[style])
    result = generate(client)
    for image in result[3]['value']:
        image_path = Path(image['name'])
        target_path = base_path / image_path.name
        shutil.copyfile(image_path, target_path)


if __name__ == '__main__':
    main()

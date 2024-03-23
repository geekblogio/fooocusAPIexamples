from gradio_client import Client
from pathlib import Path
import shutil

from helper import set_parameters, generate


def main():
    positive_prompt = 'Pomsky'
    negative_prompt = ''
    seed = 0

    cwd = Path.cwd()
    base_path = cwd / 'images' / 'simple_gen_image'
    base_path.mkdir(exist_ok=True, parents=True)

    client = Client('http://localhost:7865', serialize=False)
    if set_parameters(client, positive_prompt=positive_prompt, negative_prompt=negative_prompt, seed=seed):
        result = generate(client)
        for image in result[3]['value']:
            image_path = Path(image['name'])
            target_path = base_path / image_path.name
            shutil.copyfile(image_path, target_path)


if __name__ == '__main__':
    main()

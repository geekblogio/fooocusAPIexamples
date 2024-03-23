# helper.py

# Constants for the placeholder PNG image data
MIN_PNG = ('data:image/png;base64,'
           'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=')


def set_parameters(client, positive_prompt='', negative_prompt='', seed=0):
    result = client.predict(
        False,              # bool | toggle if an image grid gor that batch should be created
        positive_prompt,    # str | Positive Prompt
        negative_prompt,    # str | Negative Prompt
        [],                 # List[str] | Selected Styles
        'Speed',            # str | Performance: Speed, Quality, Extreme Speed, Lightning
        '1024×1024',        # str | Aspect Ratio
        1,                  # int | Number of Images to create (value between 1 and 32)
        'png',              # str | Output Format: png, jpeg, webp
        str(seed),          # str | Seed
        False,              # bool | Read wildcards in order
        2.0,                # int / float | Image Sharpness (value between 0.0 and 30.0)
        3.0,                # int / float | Guidance Scale (value between 1.0 and 30.0)
        'juggernautXL_v8Rundiffusion.safetensors',  # str | Base Model (SDXL only)
        'None',             # str | Refiner (SDXL or SD 1.5)
        0.1,                # int / float | Refiner Switch At (value between 0.1 and 1.0)
        False,              # bool | toggle LoRA 1
        'None',             # str | LoRA 1
        1.0,                # int / float | LoRA 1 Weight (value between -2.0 and 2.0)
        False,              # bool | toggle LoRA 2
        'None',             # str | LoRA 2
        1.0,                # int / float | LoRA 2 Weight (value between -2.0 and 2.0)
        False,              # bool | toggle LoRA 3
        'None',             # str | LoRA 3
        1.0,                # int / float | LoRA 3 Weight (value between -2.0 and 2.0)
        False,              # bool | toggle LoRA 4
        'None',             # str | LoRA 4
        1.0,                # int / float | LoRA 4 Weight (value between -2.0 and 2.0)
        False,              # bool | toggle LoRA 5
        'None',             # str | LoRA 5
        1.0,                # int / float | LoRA 5 Weight (value between -2.0 and 2.0)
        False,              # bool | Input Image
        '',                 # str | parameter_91 Textbox component
        'Disabled',         # str | Upscale or Variation
        MIN_PNG,            # str | Image
        [],                 # List[str] | Outpaint Direction
        MIN_PNG,            # str | inpaint or outpaint image
        '',                 # str | Inpaint Additional Prompt
        MIN_PNG,            # str | Mask Image
        True,               # bool | Disable Preview
        True,               # bool | Disable Intermediate Results
        False,              # bool in 'Disable seed increment' Checkbox component
        1.5,                # int / float | Positive ADM Guidance (value between 0.1 and 3.0)
        0.8,                # int / float | Negative ADM Guidance (value between 0.1 and 3.0)
        0.3,                # int / float | ADM Guidance End At Step (value between 0.0 and 1.0)
        7,                  # int / float | CFG Mimicking from TSNR (value between 1.0 and 30.0)
        'dpmpp_2m_sde_gpu',     # str | Sampler
        'karras',           # str | Scheduler
        -1,                 # int | Forced Overwrite of Sampling Step (value between -1 and 200)
        -1,                 # int | Forced Overwrite of Refiner Switch Step (value between -1 and 200)
        -1,                 # int | Forced Overwrite of Generating Width (value between -1 and 200)
        -1,                 # int | Forced Overwrite of Generating Height (value between -1 and 200)
        -1,                 # int | Forced Overwrite of Denoising Strength of "Vary" (value between -1 and 200)
        -1,                 # int | Forced Overwrite of Denoising Strength of "Upscale" (value between -1 and 200)
        False,              # bool | Mixing Image Prompt and Vary/Upscale
        False,              # bool | Mixing Image Prompt and Inpaint
        False,              # bool | Debug Preprocessors
        False,              # bool | Skip Preprocessors
        64,                 # int | Canny Low Threshold (value between 1 and 255)
        128,                # int | Canny High Threshold (value between 1 and 255)
        'joint',            # str | Refiner swap method
        0.25,               # int / float | Softness of ControlNet (value between 0.0 and 1.0)
        False,              # bool | toggle FreeU
        1.01,               # int / float | B1 (value between 0 and 2)
        1.02,               # int / float | B2 (value between 0 and 2)
        0.99,               # int / float | S1 (value between 0 and 4)
        0.95,               # int / float | S2 (value between 0 and 4)
        False,              # bool | Debug Inpaint Preprocessing
        False,              # bool | Disable initial latent in inpaint
        'None',             # str | Inpaint Engine
        1.0,                # float | Inpaint Denoising Strength (value between 0.0 and 1.0)
        0.618,              # float | Inpaint Respective Field (value between 0.0 and 1.0)
        False,              # bool | Enable Mask Upload
        False,              # bool | Invert Mask
        0,                  # int | Mask Erode or Dilate (value between -64 and 64)
        True,               # bool | Save Metadata to Images
        'fooocus',          # str | Metadata Scheme
        MIN_PNG,            # str Image for Image Prompt
        0.0,                # float | Stop At (value between 0.0 and 1.0)
        0.0,                # float | Weight (value between 0.0 and 2.0)
        'ImagePrompt',      # str | Type
        MIN_PNG,            # str Image for Image Prompt
        0.0,                # float | Stop At (value between 0.0 and 1.0)
        0.0,                # float | Weight (value between 0.0 and 2.0)
        'ImagePrompt',      # str | Type
        MIN_PNG,            # str Image for Image Prompt
        0.0,                # float | Stop At (value between 0.0 and 1.0)
        0.0,                # float | Weight (value between 0.0 and 2.0)
        'ImagePrompt',      # str | Type
        MIN_PNG,            # str Image for Image Prompt
        0.0,                # float | Stop At (value between 0.0 and 1.0)
        0.0,                # float | Weight (value between 0.0 and 2.0)
        'ImagePrompt',      # str | Type
        fn_index=40
    )

    if result == ():
        return True
    return False


def generate(client):
    result = client.predict(fn_index=41)
    return result

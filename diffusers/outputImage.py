from diffusers import AutoPipelineForText2Image
import torch
prompt = "a standing pikachu standing on his hands"

pipeline = AutoPipelineForText2Image.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
pipeline.load_lora_weights("E:\homework\MVClab\imgFolder\\rfes\checkpoint-60", weight_name="pytorch_lora_weights.safetensors")
image = pipeline(prompt).images[0]
image.save(prompt+".png")
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/X3WkcXtG)

# diffusion model with lora

  照著https://huggingface.co/docs/diffusers/en/training/lora的教學

  ```bash
  

  git clone https://github.com/huggingface/diffusers

  cd diffusers

  pip install .

  cd examples/text_to_image

  pip install -r requirements.txt
```

以下是啟動用的script,在cmd裡面跑

```
accelerate launch train_text_to_image_lora.py --pretrained_model_name_or_path="runwayml/stable-diffusion-v1-5" --dataset_name="E:\\homework\\MVClab\\imgFolder\\train" --dataloader_num_workers=0 --resolution=512 --center_crop --random_flip --train_batch_size=1 --gradient_accumulation_steps=1 --max_train_steps=200 --learning_rate=1e-04 --max_grad_norm=1 --lr_scheduler="linear" --lr_warmup_steps=0 --output_dir="E:\\homework\\MVClab\\imgFolder\\rfes" --report_to=wandb --checkpointing_steps=20 --validation_prompt="standing pikachu" --seed=1337
```


# diffusion model with lora

  照著https://huggingface.co/docs/diffusers/en/training/lora的教學

  ```bash
  

  git clone https://github.com/huggingface/diffusers

  cd diffusers

  pip install .

  cd examples/text_to_image

  pip install -r requirements.txt
```

以下是啟動用的script,在cmd裡面跑，用的是stable diffusion 1-5

```
accelerate launch train_text_to_image_lora.py --pretrained_model_name_or_path="runwayml/stable-diffusion-v1-5" --dataset_name="E:\\homework\\MVClab\\imgFolder\\train" --dataloader_num_workers=0 --resolution=512 --center_crop --random_flip --train_batch_size=1 --gradient_accumulation_steps=1 --max_train_steps=200 --learning_rate=1e-04 --max_grad_norm=1 --lr_scheduler="linear" --lr_warmup_steps=0 --output_dir="E:\\homework\\MVClab\\imgFolder\\rfes" --report_to=wandb --checkpointing_steps=20 --validation_prompt="standing pikachu" --seed=1337
```

不知道是他本來就有皮卡丘還是怎樣，我訓練60 step看起來就挺合理的

![image](https://github.com/mvclab-ntust-course/course3-benson5104/assets/113347980/3d414f1b-d85e-4172-bfc1-2cec407545f4)

然後最後再用outputimage.py改裡面的prompt來產出圖片

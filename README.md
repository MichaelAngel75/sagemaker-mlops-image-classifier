# ✅ One-cell solution to generate README.md completely
import os

with open("README.md", "w") as f:
    f.write("""# Final Project: Image Classification using SageMaker and Custom Container

This project implements a machine learning workflow to classify images (e.g., bicycle vs motorcycle) using AWS SageMaker Studio. It uses a pretrained container hosted on Amazon ECR, along with custom `.lst` manifest files and S3 storage for data and model artifacts.

---

## 🚀 Project Setup

### 1. Clone the Udacity Starter Repository

```bash
git clone https://github.com/udacity/udacity-nd009t-C2-Developing-ML-Workflow.git
cd udacity-nd009t-C2-Developing-ML-Workflow
```

### 2. Open SageMaker Studio and Launch Notebook

Open the `starter.ipynb` notebook from the following path in SageMaker Studio:

📎 [starter.ipynb in JupyterLab](https://kk95za7le56wapk.studio.us-east-1.sagemaker.aws/jupyterlab/default/lab/tree/udacity-nd009t-C2-Developing-ML-Workflow/project/starter.ipynb)

---

## 📂 Data Setup

Manifest files for training and testing are stored in the S3 root bucket:

- `train.lst`
- `test.lst`

Make sure the notebook references these files correctly when preparing the input for model training.

---

## 🧠 Model Training

Model artifacts will be saved to:

```bash
s3://pytorch-aws-ml-workflow/models/image_model
```

Update the SageMaker Estimator in the notebook to output to this path.

---

## 📦 Custom Container

This project uses a prebuilt image classification container hosted on Amazon ECR:

```bash
Container Image URI:
811284229777.dkr.ecr.us-east-1.amazonaws.com/image-classification:1
```

Set this URI in the `image_uri` parameter when configuring the SageMaker `Estimator`.

---

## 📝 Notes

- The notebook trains an image classifier using `.lst` file metadata.
- Training is initiated via the `sagemaker.estimator.Estimator` class.
- Model output is stored in the specified S3 location.
- Optional: Deploy an endpoint or perform batch transform for inference.

---

## 📁 Output

After successful training, you'll have:
- A trained model in S3 (`model.tar.gz`)
- Performance metrics like accuracy
- Optionally, a SageMaker endpoint for inference
""")

print("✅ README.md created successfully.")


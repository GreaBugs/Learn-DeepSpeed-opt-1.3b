from huggingface_hub import HfApi

api = HfApi()
api.upload_file(
    path_or_fileobj="opt-1.3b",
    path_in_repo="path_in_repo",  # 上传文件在仓库中的路径
    repo_id="username/repo_name",
    repo_type="model",  # 或者 "space"
    token="your_huggingface_api_token"
)

#!/bin/bash
set -e  # 遇到错误立即退出

# # 进入脚本所在目录
# cd "$(dirname "$0")"
echo $0
# 1. 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 2. 激活虚拟环境
source venv/bin/activate

# 3. 安装依赖
echo "Installing dependencies..."
pip install -r requirements.txt

# 4. 运行测试并生成报告
echo "Running tests..."
pytest app.py \
    --junitxml=test-result/test-results.xml \
    --html=test-result/report.html \
    --self-contained-html \
    -v

# 5. 返回测试结果（pytest会自动返回0/1）
exit $?
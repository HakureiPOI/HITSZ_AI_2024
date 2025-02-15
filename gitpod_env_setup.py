#!/usr/bin/env python3

import os
import subprocess

def install_dependencies():
    """
    安装实验所需的依赖
    """
    print("正在安装依赖...")
    dependencies = [
        "xvfb",  # 虚拟显示工具
        "python3-tk",  # tkinter 图形库
        "python3-pip",  # pip 包管理器
    ]

    # 更新包列表并安装依赖
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y"] + dependencies)

    # 安装 Python 依赖
    # python_packages = [
    #     "numpy",  
    #     "matplotlib", 
    # ]
    # subprocess.run(["pip", "install"] + python_packages)

    print("依赖安装完成！")

def setup_environment():
    """
    设置环境变量
    """
    print("正在设置环境变量...")
    # 设置 DISPLAY 环境变量
    os.environ["DISPLAY"] = ":1"
    print(f"DISPLAY 环境变量已设置为: {os.environ['DISPLAY']}")

def main():
    print("=== Gitpod 实验环境配置脚本 ===")
    install_dependencies()
    setup_environment()

if __name__ == "__main__":
    main()
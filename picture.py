import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# 设置中文字体（根据你的系统调整，Windows通常是SimHei，Mac是Arial Unicode MS或Heiti TC）
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

def create_3d_plot():
    fig = plt.figure(figsize=(10, 8), dpi=300)
    ax = fig.add_subplot(111, projection='3d')

    # --- 1. 数据定义 ---
    # 中国方案数据 (红色系)
    X_cn = np.array([[0, 1], [0, 1]])
    Y_cn = np.array([[0, 0], [0.3, 0.3]])
    Z_cn = np.array([[0, 0], [0.3, 0.3]])

    # 欧美方案数据 (蓝色系)
    X_us = np.array([[0, 0.6], [0, 0.6]])
    Y_us = np.array([[0, 0], [1, 1]])
    Z_us = np.array([[0, 0], [1, 1]])

    # --- 2. 绘制曲面 ---
    # 自定义渐变色
    cmap_cn = LinearSegmentedColormap.from_list('cn', ['red', 'orange'])
    cmap_us = LinearSegmentedColormap.from_list('us', ['blue', 'cyan'])

    ax.plot_surface(X_cn, Y_cn, Z_cn, cmap=cmap_cn, alpha=0.7, edgecolor='none')
    ax.plot_surface(X_us, Y_us, Z_us, cmap=cmap_us, alpha=0.6, edgecolor='none')

    # --- 3. 坐标轴设置 ---
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1.2)
    ax.set_zlim(0, 1.2)
    
    # 隐藏刻度数字，只保留轴标签
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    ax.set_xlabel('X: 硬件工程化能力', fontsize=12, labelpad=10)
    ax.set_ylabel('Y: 农艺生物学积淀', fontsize=12, labelpad=10)
    ax.set_zlabel('Z: 数据互信与合规', fontsize=12, labelpad=10)

    # 调整视角 (View: 120, 30)
    ax.view_init(elev=30, azim=120)

    # --- 4. 添加标注 (Annotation) ---
    # 中国优势区
    ax.text(1.1, 0.1, 0.1, "中国优势区\n(极致性价比)", color='red', fontsize=10, fontweight='bold')
    # 欧美壁垒区
    ax.text(0.1, 1.1, 1.1, "欧美壁垒区\n(农艺/合规)", color='blue', fontsize=10, fontweight='bold')
    # 激烈竞争带
    ax.text(0.5, 0.5, 0.5, "激烈竞争带", color='black', fontsize=10, style='italic')

    # 保存去除多余边框
    plt.tight_layout()
    plt.savefig('competition_3d.png', transparent=False)
    print("图片已生成：competition_3d.png")

if __name__ == "__main__":
    create_3d_plot()
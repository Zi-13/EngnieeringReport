import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Surface equation coefficients (Z = HARDWARE_COEFF*X + AGRONOMY_COEFF*Y + interaction)
HARDWARE_COEFF = 0.1  # Hardware has minimal impact on compliance
AGRONOMY_COEFF = 0.8  # Agronomy has strong impact on compliance
INTERACTION_COEFF = 0.05  # Small interaction term

# Sigmoid parameters for Y-axis diminishing returns
SIGMOID_STEEPNESS = 5
SIGMOID_MIDPOINT = 0.5
SIGMOID_BASELINE = 0.7
SIGMOID_AMPLITUDE = 0.3

# Try to set Chinese font, with fallback to English
try:
    plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    USE_CHINESE = True
except Exception:
    USE_CHINESE = False

def create_3d_agriculture_structure():
    """
    Create a 3D surface plot showing the relationship between:
    - X: Hardware Engineering Capability
    - Y: Agronomic Biological Accumulation
    - Z: Data Mutual Trust & Compliance
    
    The plot demonstrates that high hardware capability (X) cannot compensate
    for lack of agronomic accumulation (Y) in achieving data compliance (Z).
    """
    fig = plt.figure(figsize=(12, 9), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    # --- 1. Create Meshgrid ---
    X = np.linspace(0, 10, 50)
    Y = np.linspace(0, 10, 50)
    X_mesh, Y_mesh = np.meshgrid(X, Y)
    
    # --- 2. Define Z Surface Function ---
    # Z increases significantly with Y (agronomy), minimally with X (hardware)
    # Using sigmoid-like function for smooth curvature
    Z_mesh = (HARDWARE_COEFF * X_mesh + 
              AGRONOMY_COEFF * Y_mesh + 
              INTERACTION_COEFF * X_mesh * Y_mesh / 10.0)
    
    # Add some curvature using sigmoid on Y axis
    # This emphasizes that Y (agronomy) has diminishing returns at high values
    Y_normalized = Y_mesh / 10.0
    sigmoid_factor = 1 / (1 + np.exp(-SIGMOID_STEEPNESS * (Y_normalized - SIGMOID_MIDPOINT)))
    Z_mesh = Z_mesh * (SIGMOID_BASELINE + SIGMOID_AMPLITUDE * sigmoid_factor)
    
    # --- 3. Plot Surface ---
    surf = ax.plot_surface(X_mesh, Y_mesh, Z_mesh, 
                           cmap=cm.viridis, 
                           alpha=0.8, 
                           edgecolor='none',
                           linewidth=0,
                           antialiased=True)
    
    # Add colorbar
    cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    if USE_CHINESE:
        cbar.set_label('合规信任度', fontsize=10)
    else:
        cbar.set_label('Compliance/Trust Level', fontsize=10)
    
    # --- 4. Define Key Positions ---
    # China's Position: High X (~8-9), Low Y (~2-3), Low Z
    china_x, china_y = 8.5, 2.5
    china_z = (HARDWARE_COEFF * china_x + 
               AGRONOMY_COEFF * china_y + 
               INTERACTION_COEFF * china_x * china_y / 10.0)
    china_y_norm = china_y / 10.0
    china_sigmoid = 1 / (1 + np.exp(-SIGMOID_STEEPNESS * (china_y_norm - SIGMOID_MIDPOINT)))
    china_z = china_z * (SIGMOID_BASELINE + SIGMOID_AMPLITUDE * china_sigmoid)
    
    # Western Giants: High Y (~8-9), High X (~6-7), High Z
    west_x, west_y = 6.5, 8.5
    west_z = (HARDWARE_COEFF * west_x + 
              AGRONOMY_COEFF * west_y + 
              INTERACTION_COEFF * west_x * west_y / 10.0)
    west_y_norm = west_y / 10.0
    west_sigmoid = 1 / (1 + np.exp(-SIGMOID_STEEPNESS * (west_y_norm - SIGMOID_MIDPOINT)))
    west_z = west_z * (SIGMOID_BASELINE + SIGMOID_AMPLITUDE * west_sigmoid)
    
    # --- 5. Add Scatter Points and Projections ---
    # China's position marker (red)
    ax.scatter([china_x], [china_y], [china_z], 
               color='red', s=200, marker='o', 
               edgecolor='darkred', linewidth=2, 
               label='China Position', zorder=10)
    
    # Western Giants position marker (blue)
    ax.scatter([west_x], [west_y], [west_z], 
               color='blue', s=200, marker='s', 
               edgecolor='darkblue', linewidth=2,
               label='Western Giants', zorder=10)
    
    # Add projection lines to base plane
    ax.plot([china_x, china_x], [china_y, china_y], [0, china_z], 
            'r--', linewidth=1.5, alpha=0.6)
    ax.plot([west_x, west_x], [west_y, west_y], [0, west_z], 
            'b--', linewidth=1.5, alpha=0.6)
    
    # Add projection to XY plane
    ax.scatter([china_x], [china_y], [0], color='red', s=50, alpha=0.3)
    ax.scatter([west_x], [west_y], [0], color='blue', s=50, alpha=0.3)
    
    # --- 6. Add Annotations ---
    if USE_CHINESE:
        # China annotation
        ax.text(china_x + 0.5, china_y - 0.5, china_z + 1.5,
                '中国位置\n(技术优势\n农艺不足)',
                color='red', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
        
        # Western Giants annotation
        ax.text(west_x - 1.5, west_y + 0.5, west_z + 1.0,
                '西方巨头\n(生物数据壁垒)',
                color='blue', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    else:
        # English fallback
        ax.text(china_x + 0.5, china_y - 0.5, china_z + 1.5,
                'China Position\n(Tech Advantage\nAg Deficit)',
                color='red', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
        
        ax.text(west_x - 1.5, west_y + 0.5, west_z + 1.0,
                'Western Giants\n(Bio-Data Wall)',
                color='blue', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    
    # --- 7. Set Axis Labels and Limits ---
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    
    if USE_CHINESE:
        ax.set_xlabel('X: 硬件工程化能力', fontsize=11, labelpad=10)
        ax.set_ylabel('Y: 农艺生物学积淀', fontsize=11, labelpad=10)
        ax.set_zlabel('Z: 数据互信与合规', fontsize=11, labelpad=10)
        ax.set_title('农业智能结构性短板分析\n(硬件优势无法弥补农艺缺失)', 
                     fontsize=13, fontweight='bold', pad=20)
    else:
        ax.set_xlabel('X: Hardware Engineering Capability', fontsize=11, labelpad=10)
        ax.set_ylabel('Y: Agronomic Biological Accumulation', fontsize=11, labelpad=10)
        ax.set_zlabel('Z: Data Mutual Trust & Compliance', fontsize=11, labelpad=10)
        ax.set_title('Agricultural Intelligence Structural Shortcomings\n(Hardware Cannot Compensate for Agronomy Deficit)', 
                     fontsize=13, fontweight='bold', pad=20)
    
    # --- 8. Set View Angle ---
    ax.view_init(elev=25, azim=45)
    
    # --- 9. Add Legend ---
    ax.legend(loc='upper left', fontsize=9)
    
    # --- 10. Add Grid ---
    ax.grid(True, alpha=0.3)
    
    # --- 11. Tight Layout and Save ---
    plt.tight_layout()
    plt.savefig('3d_ag_structure.png', dpi=300, bbox_inches='tight')
    print("✓ 3D Agriculture Structure plot generated: 3d_ag_structure.png")
    print(f"  - China Position: X={china_x}, Y={china_y}, Z={china_z:.2f}")
    print(f"  - Western Giants: X={west_x}, Y={west_y}, Z={west_z:.2f}")
    print(f"  - Z is primarily driven by Y (agronomy), not X (hardware)")

if __name__ == "__main__":
    create_3d_agriculture_structure()

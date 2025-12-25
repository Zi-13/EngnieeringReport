# Engineering Report Visualizations

This repository contains visualization scripts for the Engineering Report (工程导论).

## 3D Agriculture Structure Visualization

### Overview
The `3d_agriculture_structure.py` script generates a 3D surface plot that visualizes the structural shortcomings in agricultural intelligence development (Section 3.3).

### Concept
The visualization demonstrates three key dimensions:
- **X-axis**: Hardware Engineering Capability (硬件工程化能力)
- **Y-axis**: Agronomic Biological Accumulation (农艺生物学积淀)
- **Z-axis**: Data Mutual Trust & Compliance (数据互信与合规)

The surface equation `Z = 0.1*X + 0.8*Y` (with sigmoid curvature) shows that:
- **High hardware capability (X) alone does NOT significantly increase compliance/trust (Z)**
- **Strong agronomic accumulation (Y) is the primary driver of compliance/trust (Z)**

### Key Positions Annotated
1. **China's Position** (红色标记)
   - High Hardware Capability: X ≈ 8.5
   - Low Agronomic Accumulation: Y ≈ 2.5
   - **Result**: Low Compliance/Trust: Z ≈ 2.27
   - **Interpretation**: Technology advantage cannot compensate for agronomy deficit

2. **Western Giants** (蓝色标记)
   - Moderate Hardware: X ≈ 6.5
   - High Agronomic Accumulation: Y ≈ 8.5
   - **Result**: High Compliance/Trust: Z ≈ 7.38
   - **Interpretation**: Long-term bio-data accumulation creates barriers

### Usage

#### Requirements
```bash
pip install matplotlib numpy
```

#### Generate the Plot
```bash
python3 3d_agriculture_structure.py
```

This will generate `3d_ag_structure.png` in the current directory.

### Output
- **File**: `3d_ag_structure.png`
- **Resolution**: 300 DPI
- **Format**: PNG with transparency support
- **Size**: Approximately 740KB

### Features
- ✅ 3D surface plot with color gradient (viridis colormap)
- ✅ Two annotated key positions (China vs Western Giants)
- ✅ Projection lines to base plane for spatial clarity
- ✅ Chinese language support with English fallback
- ✅ High-resolution output suitable for reports
- ✅ Clear visualization of the relationship: Z ∝ Y >> Z ∝ X

### Interpretation
The plot visually demonstrates that in agricultural intelligence:
1. Hardware engineering alone (high X) cannot achieve high compliance/trust (Z)
2. Agronomic and biological data accumulation (high Y) is essential for trust (Z)
3. China's structural shortcoming is the lack of Y despite having high X
4. Western companies have built barriers through long-term Y accumulation

---

## Other Visualizations

### Competition 3D Plot
The `picture.py` script generates a competitive landscape visualization (`competition_3d.png`).

```bash
python3 picture.py
```

---

## License
This project is part of the Engineering Introduction course materials.

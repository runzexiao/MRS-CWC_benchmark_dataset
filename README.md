
# MRS-CWC 3D Rough Terrain Navigation Simulation Benchmark Dataset

This repository provides a **simulation-based benchmark dataset** for evaluating the performance of robotic navigation systems in **3D rugged terrains**. It is built upon [CoppeliaSim](https://www.coppeliarobotics.com/) version 4.7.0 and is suitable for testing a variety of robot control methods, including multi-robot coordination strategies.

The benchmark includes **100 unique environments**, divided into two groups:
- **`lessthan30`**: 50 terrains with average slopes < 30°
- **`morethan30`**: 50 terrains with average slopes ≥ 30°

robot should navigate from the starting point [0,0,H(0,0)] to the target [9,9,H(9,9)]. A trial was considered successful if the robot’s XY-plane projection distance
to the target fell below 0.5 m within 1000 seconds.

---

## 🚀 Features

- Standardized and reproducible benchmark framework for 3D terrain navigation
- Two environment categories with 50 variations each
- 8 configurable multi-robot navigation methods as example or baseline for evaluation
- Clear performance metrics (NSR, NCR, NEF, NEC)

---

## 📊 Evaluation Metrics

This benchmark evaluates navigation performance using the following metrics:

### 1. Navigation Success Rate (NSR)

If `Ns` is the number of successful trials among 50 terrains in one environment category:

```
NSR = Ns / 50
```

---

### 2. Navigation Completion Rate (NCR)

Let `L` be the horizontal distance from start to target, and `d` be the minimum distance reached:

```
Effective Distance Def = L - d
NCR = (L - d) / L
```

---

### 3. Navigation Efficiency (NEF)

Let `J` be the actual path length the robot traveled:

```
NEF = Def / J
```

---

### 4. Navigation Energy Consumption (NEC)

Using wheel torques (`τ`) and angular velocities (`ω`) of 6 robots over time `T`:

```
E = ∫₀ᵀ ∑ᵢ₌₁⁶ (|τL,i * ωL,i| + |τR,i * ωR,i|) dt
NEC = E / Def
```

---

## 🛠 Getting Started

### Prerequisites

- [CoppeliaSim](https://www.coppeliarobotics.com/) version **4.7.0**
- Python 3.9
- Required Python packages:
  - `coppeliasim_zmqremoteapi_client`
  - `time` (standard)
  - `os` (standard)

Install the CoppeliaSim ZMQ Python client:

```bash
pip install coppeliasim_zmqremoteapi_client
```

---

## ⚙️ How to Run the Benchmark

### Step 1: Open the Benchmark Scene

1. Launch **CoppeliaSim 4.7.0**
2. Go to **File > Open Scene...**
3. Open the file:
   ```
   coppeliasim_based_benchmark/my_method.ttt
   ```

---

### Step 2: Set Simulation Settings

In CoppeliaSim, go to **Simulation > Simulation settings**, and set:

- **Simulation time step** = `0.025` seconds
- **Dynamics time step** = `0.0025` seconds

---

### Step 3: Configure and Run the Controller

Edit `simulation_controller.py` to select the environment and method:

```python
environment_type = "lessthan30"  # or "morethan30"
environment_num = 1              # from 1 to 50
method = "my_method"             # see method list below
```

Supported methods:

- `my_method`
- `my_method_pathplan`
- `constantly_soft`
- `constantly_soft_pathplan`
- `distribute`
- `distribute_pathplan`
- `motorized_joint`
- `motorized_joint_pathplan`

Then run:

```bash
python simulation_controller.py
```

The evaluation metrics from each simulation will be stored in the simulation_result_for_user folder. Note that results from the same environment type and method will be written into the same CSV file.

---

## 📄 License

This benchmark is released under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

## 📬 Contact

If you have any questions or suggestions, feel free to contact:

**Runze Xiao (肖潤沢)**  
Postdoctoral Researcher, The University of Tokyo  
Email: runzexiao@g.ecc.u-tokyo.ac.jp

---

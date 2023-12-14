# RL Project 2023.12.18
<p align="center">
	<img src="https://github.com/zyounguri/RL/assets/138076274/25fdba84-a836-4234-977a-f050752cf0e3" alt="viz_doom제목"/>
</p>	
This project began as part of the Reinforcement Learning course at the University of Seoul.
<br><br>

![vizdoom-demo](https://github.com/zyounguri/RL/assets/138076274/9e5ad5d6-0c5e-4068-aca2-b114303b36bb)


## Scenario
<img src="https://github.com/zyounguri/RL/assets/138076274/31d6cada-7cab-41c8-b268-73437a2c9e50" align="left" width="450"/> 


###  **Task**
: Shoot randomly generated targets on the opposite wall with a gun.

###  **Actions**
: 3 actions [Left, Right, Shot]

###  **Reward Design**
-1 if 1 frame has passed
-5 if shot missed
+100 if shot hit

###  **Episode Termination**
(1)-if 200 frames have passed
<br>(2)-if enemy is hit

<br><br><br>
## Code

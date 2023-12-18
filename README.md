# RL Project 2023.12.18
<p align="center">
	<img src="https://github.com/zyounguri/RL/assets/138076274/25fdba84-a836-4234-977a-f050752cf0e3" alt="viz_doom제목" width=450/>
</p>	
This project began as part of the Reinforcement Learning course at the University of Seoul.
<br><br>

![vizdoom-demo](https://github.com/zyounguri/RL/assets/138076274/9e5ad5d6-0c5e-4068-aca2-b114303b36bb)


## Scenario
<img src="https://github.com/zyounguri/RL/assets/138076274/31d6cada-7cab-41c8-b268-73437a2c9e50" align="left" width="500"/> 


###  **Task**
: Shoot randomly generated targets on the opposite wall with a gun.

###  **Actions**
: 3 actions [Left, Right, Shot]

###  **Reward Design**
-1 if 1 frame has passed
-5 if shot missed
+100 if shot hit

###  **Episode Termination**
(1) 200 frame timeout
(2) enemy hit

<br>

## **Files**
Warning: You might have to tune some file paths in the code.
<br><br>
**basic.py**
<br>Run to test basic random policy agent in ViZDoom environment.
<br><br>
**no_trained_base_model.py**
<br>Run to test initialized CNN-based agent.
<br><br>
**trained_base_model.py**
<br>You can make model trained with ViZDoom scenario by REINFORCE policy gradient.
<br>Reward and Loss will be saved during training every episodes.
<br>Your trained model will be saved every after 10000 episodes.
<br><br>
**gradient_accumulation.py**
<br>This is a version with gradient accumulation algorithm added to the trained_base_model.py.
<br>Except for that, everything else is the same.
<br><br>
**play_model.py**
<br>You can see how your trained agent play ViZDoom scenario well via this file.
<br>Note that this file has to be excuted in terminal.
<br>How to excute this file is writed at the last line of the file.
<br><br>
**graph_log.py**
<br>Produces *graph.png* file via log.txt or acc_log.txt.
<br>Tune some variables to tune value for x or y axis.
<br><br>
**model.py**
<br>CNN model is factorized in this file.
<br><br>
**for_ppt.py**
<br>It's just a dump file.
<br><br>

## Contributors
**Jeonghyun Kim** 📧 kr.jeonghyun.kim@gmail.com
<br><br>**Jiyoung Seo** 📧 tjwldud0531@naver.com
<br><br>

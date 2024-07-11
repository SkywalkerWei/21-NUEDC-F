#pid巡线前进
def lookfor_line():
    # 使用PID算法计算控制信号
    rho_output = rho_pid.get_pid(直线平移偏移量, 1)
    theta_output = theta_pid.get_pid(直线旋转偏移量, 1)
    output = rho_output + theta_output
    # 根据PID输出调整小车的速度
    output = output * 2
    car.run(80+ output, 80 - output)
 
 
# 计算直线的平移偏移量（直线中点到图像中心的距离）
直线平移偏移量 = abs(line.rho()) - img.width() / 2
# 计算直线的旋转偏移量（直线与垂直方向的夹角）
if line.theta() > 90:
    直线旋转偏移量 = line.theta() - 180
else:
    直线旋转偏移量 = line.theta()

stats = img.get_statistics()
# 如果直线的强度（长度）足够大，则认为是有效直线，需要控制小车
if stats.mean() > 3:
    lookfor_line()

#遇到了路口
if stats.mean()>18:

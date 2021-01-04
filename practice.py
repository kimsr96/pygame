balls = []

balls.append({
    "pos_x": 50, #공의 x좌표
    "pos_y":50, #공의 y좌표
    "img_idx":0, #공의 이미지 인덱스
    "to_x":3, #x축 이동방향, -3이면 왼쪽으로 , 3이면 오른쪽으로
    "to_y":-6, # y축 이동방향,
    # "init_spd_y":ball_speed_y[0]
})

for ball_idx, ball_val in enumerate(balls):
        print(ball_idx,ball_val["pos_x"])
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        print(ball_pos_x,ball_pos_y,ball_img_idx)
        # ball_size = ball_images[ball_img_idx].get_rect().size
        # ball_width = ball_size[0]
        # ball_height = ball_size[1]

def on_button_pressed_a():
    if 篮子.get(LedSpriteProperty.X) > 0:
        篮子.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if 篮子.get(LedSpriteProperty.X) < 4:
        篮子.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

篮子: game.LedSprite = None
鸡蛋 = game.create_sprite(randint(0, 5), 0)
game.set_score(0)
篮子 = game.create_sprite(2, 4)

def on_forever():
    if 篮子.is_touching(鸡蛋):
        game.game_over()
    elif 鸡蛋.get(LedSpriteProperty.Y) < 4:
        鸡蛋.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    else:
        鸡蛋.set(LedSpriteProperty.Y, 0)
        鸡蛋.set(LedSpriteProperty.X, randint(0, 5))
basic.forever(on_forever)

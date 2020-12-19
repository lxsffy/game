input.onButtonPressed(Button.A, function () {
    if (篮子.get(LedSpriteProperty.X) > 0) {
        篮子.change(LedSpriteProperty.X, -1)
    }
})
input.onButtonPressed(Button.B, function () {
    if (篮子.get(LedSpriteProperty.X) < 4) {
        篮子.change(LedSpriteProperty.X, 1)
    }
})
let 篮子: game.LedSprite = null
let 鸡蛋 = game.createSprite(randint(0, 5), 0)
game.setScore(0)
篮子 = game.createSprite(2, 4)
basic.forever(function () {
    if (篮子.isTouching(鸡蛋)) {
        game.gameOver()
    } else if (鸡蛋.get(LedSpriteProperty.Y) < 4) {
        鸡蛋.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    } else {
        鸡蛋.set(LedSpriteProperty.Y, 0)
        鸡蛋.set(LedSpriteProperty.X, randint(0, 5))
    }
})

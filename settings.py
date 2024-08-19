#Display settings
DEFAULT_IMAGE_SIZE = (300,300)
FPS = 120
HEIGHT = 1024
WIDTH = 1024
START_X, START_Y = 0 , -300
X_OFFSET, Y_OFFSET = 20, 0

#Images
BG_IMAGE_PATH = 'graphics/neon/pozadina.jpg'
GAME_INDICES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = 'graphics/0/symbols'

# 5 Symbols for testing
symbols = {
    'zeus': f"{SYM_PATH}/0_zeus.png",
    'atena': f"{SYM_PATH}/0_atena.png",
    'ares': f"{SYM_PATH}/0_ares.png",
    'm': f"{SYM_PATH}/0_M.png",
    'l': f"{SYM_PATH}/0_L.png",
    'd': f"{SYM_PATH}/0_D.png",
    'sketer': f"{SYM_PATH}/0_sketer.png",
    'c': f"{SYM_PATH}/0_C.png"
}
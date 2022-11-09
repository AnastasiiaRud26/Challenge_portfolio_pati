from pages.base_page import BasePage


class Dashboard(BasePage):
    button_main_page = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    button_players = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/spanv"
    button_polski = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    button_sing_out = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    button_dev_team_contact = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    button_add_player = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    button_kla_kla = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    button_fd_dfg = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    button_legia_warszawa = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    space_scout_panel = "//*[@id="__next"]/div[1]/header/div/h6"
    space_matches_count = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[1]"
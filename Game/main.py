import pygame
import collisions
import event
import gamestate


was_closed = False
while not was_closed:
    game = gamestate.GameState()
    game.start_pool()
    events = event.events()
    while not (events["closed"] or game.is_game_over):
        events = event.events()
        collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
        game.redraw_all()

        if game.all_not_moving():
            game.check_pool_rules()
            game.cue.make_visible(game.current_player)
            while not (events["closed"] or game.is_game_over) and game.all_not_moving():
                game.redraw_all()
                events = event.events()
                if game.cue.is_clicked(events):
                    game.cue.cue_is_active(game, events)
    was_closed = events["closed"]

pygame.quit()

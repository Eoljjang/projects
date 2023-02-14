# Mini Project #2 - Nathan Wong
# NOTE: The game requires the user to press the spacebar before it begins. This was done for organizational purposes and intuitivity of the game.
# NOTE: Player_1 movement is handled with the 'w' and 's' keys, while player_2 movement is handled with the 'up arrow' and 'down arrow' keys.

# Modules
import pygame

# Main 
def main():
    pygame.init()
    
    # Create display window:
    width = 500
    height = 400
    pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pong')
    
    # get the display surface
    w_surface = pygame.display.get_surface()    

    # Create 'game' object
    game = Game(w_surface, width, height)
    
    # Start gameplay loop
    game.play()
    
    # Quit pygame and clean up window
    pygame.quit()

class Game:
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width = width
        self.height = height
        self.bg_color = pygame.Color('Black')
        self.object_color = pygame.Color('White')
        
        self.FPS = 60
        self.game_clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = False # Is changed to 'True' once the the spacebar is pressed (see comment on line #2)
        
        # Paddle objects (surface, color, x_co, y_co, width, height)
        self.paddle_1 = Paddle(self.surface, self.object_color, self.width//15, height//2 - 35, 5, 70)
        self.paddle_2 = Paddle(self.surface, self.object_color, self.width - 5 - self.width//15, height//2 - 35, 5, 70)
        
        # Game ball + Collision Object
        self.game_ball = Ball(self.surface, self.object_color, [self.width//2, self.height//2], 10, [5, 5])
        self.collision = Collisions(self.surface)
        
        # Scorecounter
        self.score_1 = 0
        self.score_2 = 0
       
    # Play game until the exit box is clicked.
    def play(self):
        while not self.close_clicked:
            self.handle_events()
            self.draw()
            
            # Game happens here:
            if self.continue_game:
                self.update()
            
            self.game_clock.tick(self.FPS)
    
    # Events the players may execute.
    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            
            # The game doesn't start until the 'space' key is pressed, and paddles cannot be moved until the game starts.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.continue_game = True
                
                # Paddle movement
                if event.key == pygame.K_w:
                        self.paddle_1.state = 'up'
                    
                if event.key == pygame.K_s:
                        self.paddle_1.state = 'down'
                    
                if event.key == pygame.K_UP:
                        self.paddle_2.state = 'up'
                    
                if event.key == pygame.K_DOWN:
                        self.paddle_2.state = 'down'
            
            # If the player is not pressing the above keys, the paddles won't move. IE: No keys are pressed.
            elif event.type == pygame.KEYUP:
                self.paddle_1.state = 'stopped'
                self.paddle_2.state = 'stopped'
    
    # Scoreboard
    def draw_score(self, object_color, bg_color):
        player1_string = '' + str(self.score_1)
        player2_string = '' + str(self.score_2)
        font_size = 50
        font_name = 'Times New Roman'
        self.object_color = object_color
        self.bg_color = bg_color
        
        # Create font object
        font = pygame.font.SysFont(font_name, font_size)
        
        # Render font object
        player1_points = font.render(player1_string, True, self.object_color, self.bg_color)
        player2_points = font.render(player2_string, True, self.object_color, self.bg_color)
        
        # Locations
        textbox_width = player2_points.get_width()
        player1_location = (0,0)
        player2_location = (self.width - textbox_width, 0)
        
        # Draw (blit) text object onto surface
        self.surface.blit(player1_points, player1_location)
        self.surface.blit(player2_points, player2_location)
        
                
    # Draw all the game objects
    def draw(self):
        self.surface.fill(self.bg_color)
  
        # Middle line
        pygame.draw.line(self.surface, self.object_color, (self.width/2, 0), (self.width/2, self.height), 2)
    
        # Draw game ball
        self.game_ball.draw()
        
        # Draw player paddles
        self.paddle_1.draw()
        self.paddle_2.draw()
        self.draw_score(self.object_color, self.bg_color)
        
        # display the updated surface
        pygame.display.update()        
        
    
    # Updates the game objects for the next frame.
    def update(self):
        point_won = ''
        end_score = 11
        # Call the 'move' function for the game_ball
        point_won = self.game_ball.move()
        
        # Check for points
        if point_won == 'hit right':
            self.score_1 += 1
        
        elif point_won == 'hit left':
            self.score_2 += 1
            
        # Call the 'move' function when players move the paddles
        self.paddle_1.move()
        self.paddle_2.move()
        
        # Check for paddle collisions
        if self.collision.ball_hits_paddle(self.game_ball, self.paddle_1) or self.collision.ball_hits_paddle(self.game_ball, self.paddle_2):
            self.game_ball.paddle_collision()
        
        # Draw score
        self.draw_score(self.object_color, self.bg_color)
        
        # Game ends once desired score is reached
        if self.score_1 == end_score or self.score_2 == end_score:
            self.continue_game = False
    

class Ball:
    def __init__(self, surface, color, center, radius, ball_velocity):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.ball_velocity = ball_velocity
    
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
    
    def move(self):
        # Find the bounds of the window
        size = self.surface.get_size()
        point_won = ''
        
        # The ball moves
        for i in range(0, 2):
            # 'Movement'
            self.center[i] = (self.center[i] + self.ball_velocity[i])
            
            # Ball hits left wall
            if self.center[i] <= self.radius:
                self.ball_velocity[i] = -self.ball_velocity[i]
                self.center[i] = (self.center[i] + self.ball_velocity[i])
                # If it hits the left wall, a point is won.
                if i == 0:
                    point_won = 'hit left'
                
            # Ball hits right wall    
            elif self.center[i] + self.radius >= size[i]:
                self.ball_velocity[i] = -self.ball_velocity[i]
                self.center[i] = (self.center[i] + self.ball_velocity[i])
                # If it hits right wall, a point is won.
                if i == 0:
                    point_won = 'hit right'
        
        return point_won
    
    def paddle_collision(self):
        self.ball_velocity[0] = - self.ball_velocity[0]
    

class Paddle:
    def __init__(self, surface, color, pos_x, pos_y, width, height):
        self.surface = surface
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.paddle_velocity = 10
        self.state = 'stopped'
        
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.pos_x, self.pos_y, self.width, self.height))
    
    def move(self):
        # If the state is up/down and it's within the window's boundaries, the paddle will move up/down 10 units respectively.
        if self.state == 'up' and self.pos_y > 0:
            self.pos_y -= self.paddle_velocity
        
        elif self.state == 'down' and self.pos_y < self.surface.get_height() - self.height:
            self.pos_y += self.paddle_velocity
    
    # def set_state(self, new_state):
    #     self.state = new_state 


class Collisions:
    
    def __init__(self, surface):
        self.surface = surface
        self.size = self.surface.get_size()
  
    def ball_hits_paddle(self, game_ball, paddle):
        middle = self.size[0] // 2
        
        # If the paddle is on the left side (paddle_1)
        if paddle.pos_x < middle:
            if game_ball.center[1] + game_ball.radius > paddle.pos_y and game_ball.center[1] - game_ball.radius < paddle.pos_y + paddle.height and game_ball.ball_velocity[0] < 0:
                # AND the ball is on the respective paddle's side
                if game_ball.center[0] - game_ball.radius <= paddle.pos_x + paddle.width:
                    return True
            
            return False
        
        # If the paddle is on the right side (paddle_2)
        if paddle.pos_x > middle:
            if game_ball.center[1] + game_ball.radius > paddle.pos_y and game_ball.center[1] - game_ball.radius < paddle.pos_y + paddle.height and game_ball.ball_velocity[0] > 0:
                # AND the ball is on the respective paddle's side
                if game_ball.center[0] + game_ball.radius >= paddle.pos_x:
                    return True            

            return False
    
main()

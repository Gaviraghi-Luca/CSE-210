import pyray as pr
from game.video_service import VideoService


class VideoPhysicsService(VideoService):
    """
    Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen.  
    """

    def __init__(self):
        """
        Inherits from VideoService class.
        """
        super().__init__()

    def draw_body(self, index):
        """
            Displays an existing body.
            Args:
                index (int): the index of the body in the bodies pool.
        """
        body = pr.get_physics_body(index)
        vertex_count = pr.get_physics_shape_vertices_count(index)
        for j in range(vertex_count):
            vertexA = pr.get_physics_shape_vertex(body, j)
            jj = (j + 1) if (j+1) < vertex_count else 0
            vertexB = pr.get_physics_shape_vertex(body, jj)
            if index == 0:
                pr.draw_line_v(vertexA, vertexB, pr.WHITE)
            elif index == 1:
                pr.draw_line_v(vertexA, vertexB, pr.RED)
            else:
                pr.draw_line_v(vertexA, vertexB, pr.GREEN)
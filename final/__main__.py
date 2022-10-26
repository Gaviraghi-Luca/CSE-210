import imp
from game.director import Director
from game.video_phscs_srv import VideoPhysicsService
from game.phys_service import PhysService

def main():
    video_service = VideoPhysicsService()
    physics_service = PhysService()

    director = Director(video_service, physics_service)
    director.start_game()

if __name__ == "__main__":
    main()
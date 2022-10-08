class Sprite_Collection:
    """A collection of sprites.

    The responsibility of a cast is to keep track of a collection of sprites. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _sprites (dict): A dictionary of sprites { key: group_name, value: a list of sprites }
    """

    def __init__(self):
        """Constructs a new Sprite."""
        self._sprites = {}
        
    def add_sprite(self, group, sprite):
        """Adds an Sprite to the given group.
        
        Args:
            group (string): The name of the group.
            sprite (Sprite): The Sprite to add.
        """
        if not group in self._sprites.keys():
            self._sprites[group] = []
            
        if not sprite in self._sprites[group]:
            self._sprites[group].append(sprite)

    def get_sprites(self, group):
        """Gets the sprites in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The sprites in the group.
        """
        results = []
        if group in self._sprites.keys():
            results = self._sprites[group].copy()
        return results
    
    def get_all_sprites(self):
        """Gets all of the sprites in the cast.
        
        Returns:
            List: All of the sprites in the cast.
        """
        results = []
        for group in self._sprites:
            results.extend(self._sprites[group])
        return results

    def get_first_sprite(self, group):
        """Gets the first Sprite in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first Sprite in the group.
        """
        result = None
        if group in self._sprites.keys():
            result = self._sprites[group][0]
        return result

    def remove_sprite(self, group, sprite):
        """Removes a Sprite from the given group.
        
        Args:
            group (string): The name of the group.
            sprite (Sprite): The Sprite to remove.
        """
        if group in self._sprites:
            self._sprites[group].remove(sprite)
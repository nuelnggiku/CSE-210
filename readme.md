"""A fast motorcycle.
    The responsibility of Cycle is to move itself.
    Attributes:
    ---
        _segments (list): A list of actors that make up each cycle.
        _color (tuple): A tuple containing the values that make up a color.
        _prepare_cycle (method): A method that will create the cycle for each instance of Cycle.
        _name (str): An empty string that will hold each players name.
    """

     """Constructs a new cycle.
        Args:
        ---
            position (Point): The position and direction that each cycle will travel in at game start.
        """

         """Gets the segments for each cycle.
        Returns:
        ---
            List: The list of actors for each cycle"""

              """Gets the players name.
        Returns:
        ---
            String: The players name as text."""

              """Moves the actor to its next position according to its velocity. Will move each actor
        in _segments beginning from the last segment and ending with the first segment and
        stepping by -1 to iterate through the last backwards."""

         """Gets the first actor from _segments.
        Returns:
        ---
            Actor: The first actor from the list of actors in _segments."""

            """Builds the wall for each cycle.
        Args:
        ---
            Boolean: Sets the color for each cycle if game is not over. Changes each
            cycle color to white if game is over.
        """
  """Constructs a new cycle.
        Args:
        ---
            Point: A position to set the cycle position and direction which it will travel in.
        """

         """Sets the color for each segment of a cycle.
        Args:
        ---
            color (Color): The given color.
        """
        
          """Sets the name for each player.
        Args:
        ---
            String: The players given name as text.
        """



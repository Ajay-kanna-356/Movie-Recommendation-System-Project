from typing import List, Optional

# Base Filter Strategy
class FilterStrategy:
    def filter(self, movies: List[List]) -> List[List]:
        return movies

# Concrete Strategy for each filtering criterion
class GenreFilter(FilterStrategy):
    def __init__(self, genre: str):
        self.genre = genre

    def filter(self, movies: List[List]) -> List[List]:
        return [movie for movie in movies if movie[1] == self.genre]

class RatingFilter(FilterStrategy):
    def __init__(self, rating: float):
        self.rating = rating

    def filter(self, movies: List[List]) -> List[List]:
        return [movie for movie in movies if movie[2] >= float(self.rating)]

class DirectorFilter(FilterStrategy):
    def __init__(self, director_name: str):
        self.director_name = director_name

    def filter(self, movies: List[List]) -> List[List]:
        return [movie for movie in movies if movie[3].lower() == self.director_name.lower()]

# Decorator that allows chaining of filters
class FilterDecorator(FilterStrategy):
    def __init__(self, strategy: FilterStrategy, decorator: FilterStrategy):
        self._strategy = strategy
        self._decorator = decorator

    def filter(self, movies: List[List]) -> List[List]:
        # Apply the decorated strategy first, then apply the base strategy
        filtered_movies = self._decorator.filter(movies)
        return self._strategy.filter(filtered_movies)

# Function to apply filters dynamically with layering
def apply_filters_facade(movies: List[List], genre: Optional[str] = None, 
                  rating: Optional[float] = None, 
                  director_name: Optional[str] = None) -> List[List]:
    
    # Start with the base filter (no filtering)
    filter_strategy = FilterStrategy()
    
    # Wrap each filter around the previous one, creating layers
    if genre:
        filter_strategy = FilterDecorator(GenreFilter(genre), filter_strategy)
    if rating:
        filter_strategy = FilterDecorator(RatingFilter(rating), filter_strategy)
    if director_name:
        filter_strategy = FilterDecorator(DirectorFilter(director_name), filter_strategy)
    
    # Apply the stacked filters to the movies list
    return filter_strategy.filter(movies)
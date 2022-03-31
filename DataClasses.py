#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (James Miller, 3/27/22, filled out Track class and added track compatability to CDs)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    def __init__(self, position, title, length):
        ''' base variables for tracks'''
        self.__tp = position
        self.__tt = title
        self.__tl = length
    ''' A certain someone thought I needed to add an entire command for the doc function to print the memo, 
    but I just needed to move the docstring back to the top
    def __doc__():
        print('Stores Data about a single Track:\n\n\tproperties:\n\t\tposition: (int) with Track position on CD/Album')
        print('\t\ttitle: (str) with Track title\n\t\tlength: (str) with length / playtime of Track')
        print('\tmethods:\n\t\tget_record() -> (str)')
        return    
    '''
    @property
    def tp(self):
        return self.__tp
    @tp.setter
    def tp(self, position):
        '''checks position can be a valid int updating value'''
        try:
            target = int(position)
            self.__tp = target
        except:
            print('Error: Position should be an integer')
    @property
    def tt(self):
        return self.__tt
    @tt.setter
    def tt(self, title):
        '''checks title can be a valid string before updating value'''
        try:
            target = str(title)
            self.__tt = target
        except:
            print('Error: Title not recognized as text')
    @property
    def tl(self):
        return self.__tl
    @tl.setter
    def tl(self, length):
        '''checks length can be a valid string before updating value'''
        try:
            target = str(length)
            self.__tl = target
        except:
            print('Error: Length not a recognized input')


    def __str__(self):
        """Returns Track details as formatted string"""
        script = '{}, {}, {}'.format(self.tp,self.tt,self.tl)
        return script
        pass

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        script = '{},{},{}\n'.format(self.tp,self.tt,self.tl)
        return script


class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__tracks

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        self.__tracks.append(track)
        self.__sort_tracks()
        
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """
        flag = 'no'
        for track in self.__tracks:
            if track.tp == track_id:
                self.__tracks.remove(track)
                print('Removed the track with position id '+str(track_id))
                flag = 'yes'
        if flag == 'no':
            print('Could not find a track with position id '+str(track_id))
        self.__sort_tracks()
            


    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.tp):
                n = track.tp
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.tp - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result





#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (James Miller, 3/29/22, Added functions for selecting cds and adding tracks)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        try:
            target = int(cd_idx)
        except Exception as e:
            print('ID not recognized as a integer')
            print(e.__doc__)
            target = cd_idx
        for item in table:
            if item.cd_id == target:
                return item
        print('Could not locate a matching cd')
        return


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        (tp, tt, tl) = track_info
        try:
            tp = int(tp)
        except:
            print('Error, track position not recognized as a number')
        try:
            track = DC.Track(tp,tt,tl)
            cd.add_track(track)
        except:
            print('Error encountered with adding new track')


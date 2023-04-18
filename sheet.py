import gspread

# Authenticate with Google Sheets API
sa = gspread.service_account()


class Birthdays():
    def __init__(self) -> None:
        # Name of the Google Sheets file
        self.filename = "google sheet file name here"
        # Open the file and select the worksheet
        self.spreadsheet = sa.open(self.filename)
        self.main_worksheet = self.spreadsheet.worksheet("sheet name here")

    def get_name(self, date: str):
        # Find all cells with the specified date
        matching_cells = self.main_worksheet.findall(date)
        if not matching_cells:
            return []
        # Get names in the first column of each matching cell's row
        names = [self.main_worksheet.cell(cell.row, 1).value for cell in matching_cells]
        # Filter Nones
        names = [name for name in names if name is not None]
        return names


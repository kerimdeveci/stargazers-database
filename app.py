import data_manager as dt

if __name__ == "__main__":
    manager = dt.data_manager('kerimdeveci', 'data4')
    values = manager.fetch_data()
    manager.write_col(values)

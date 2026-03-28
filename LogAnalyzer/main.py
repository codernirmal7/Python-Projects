from log_analyzer import LogAnalyzer

def main () :
    analyzer =  LogAnalyzer("server.log")
    analyzer.load_logs()

    while True :
        print("\nLog Analyzer")
        print("1. Show all logs")
        print("2. Count log levels")
        print("3. Show only errors")
        print("4. Search logs")
        print("5. Filter by date")
        print("6. Logs Report export")
        print("7. Sort logs")
        print("8. Exit")


        choice = input("Choose option : ")

        match choice :
            case "1" :
                analyzer.show_all_logs()
            case "2" :
                counts = analyzer.count_log_levels()
                for level, count in counts.items():
                    print(f"{level}: {count}")
            case "3" :
                 analyzer.show_only_errors()
            case "4" :
                 analyzer.search_logs()
            case "5" :
                 analyzer.filter_by_date()
            case "6" :
                 analyzer.export_report()
            case "7" :
                 analyzer.sort_logs()
            case "8" :
                break
            case _ :
                print("Invalid choice!")

if __name__ == "__main__" :
    main()

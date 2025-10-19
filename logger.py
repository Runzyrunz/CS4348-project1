import sys
import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    try: 
        with open(log_file, 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"{timestamp} [START] logger Started. \n")

            #Process input
            while True:
                try:
                    line=input()
                    if line.strip() == "QUIT":
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                        f.write(f"{timestamp} [QUIT] logger Shutting off. \n")
                        break
                

                except EOFError:
                    break
                except Exception as e:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    f.write(f"{timestamp} [ERROR] logger error: {str(e)}\n")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

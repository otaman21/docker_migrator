import sys
import logging
import tool.args_parser
import tool.util
import connect.connection



#Parse arguments
args = tool.args_parser.parse_client_args()

#logging configuration
logging.basicConfig(filename=args.log_file,filemode="a", level=logging.INFO,
	format="%(asctime)s.%(msecs)03d: %(process)d: %(message)s",
	datefmt="%H:%M:%S")

# Setup hook to log uncaught exceptions
sys.excepthook = phaul.util.log_uncaught_exception

phaul.util.log_header()
logging.info("Starting migrate!")

#Establish connection
connection = connect.connection.establish(args.fdmem,args.fdrpc,args.fdfs)

#Start migration
controller = client.iters.migration_iter_controller(args.id,args.dst_id,connection,args.mode)
controller.set_options(vars(args))
controller.start_live_migration()
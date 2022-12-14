from BSE import market_session

start_time = 0
end_time = 60 * 60 * 24 * 100

sup_range = (60, 140)
dem_range = (60, 140)

supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [sup_range], 'stepmode': 'jittered'}]
demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [dem_range], 'stepmode': 'jittered'}]

order_interval = 60
order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
               'interval': order_interval, 'timemode': 'drip-poisson'}

sellers_spec = [('ZIC', 29), ('PRDE', 1, {'k': 4, 's_min': -1.0, 's_max': 1.0})]
buyers_spec = [('ZIC', 30)]
traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

trial = 1
trial_id = '1PRDEK4_MZIC' + str(trial)
tdump = open('1PRDEK4_MZIC' + str(trial) + '_avg_balance.csv', 'w')
dump_all = True
verbose = False
market_session(trial_id, start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose)
tdump.close()

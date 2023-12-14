import matplotlib.pyplot as plt
import json
import argparse


def run(args):
    log_rows = []
    with open(args.in_logfile) as f:
        for line in f:
            row = json.loads(line)
            log_rows.append(row)
    episodes = [row['batch'] for row in log_rows][:30000]
    losses = [row['reward'] for row in log_rows][:30000]
    # plt.plot(episodes, losses)
    # plt.savefig('./graph.png')
    episodes_avg = []
    losses_avg = []
    average_over = 10
    num_batches = len(episodes) // average_over
    for b in range(num_batches):
        b_start = b * average_over
        b_end = b_start + average_over
        avg_episode = sum(episodes[b_start:b_end]) / average_over
        avg_losses = sum(losses[b_start:b_end]) / average_over
        episodes_avg.append(avg_episode)
        losses_avg.append(avg_losses)
    plt.plot(episodes_avg, losses_avg)
    plt.savefig('./graph.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-logfile', type=str, default='acc_log.txt')
    args = parser.parse_args()
    run(args)

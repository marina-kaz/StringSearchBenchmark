import pandas as pd
from matplotlib import pyplot as plt


def plot_complexity(parameter: str, benchmark_results: pd.DataFrame):
    """
    Plot complexity depending on the parameter
    """

    if parameter == "M + N":
        param = benchmark_results.substring_length + benchmark_results.string_length
    elif parameter == "M x N":
        param = benchmark_results.substring_length * benchmark_results.string_length
    elif parameter == "M":
        param = benchmark_results.substring_length
    elif parameter == "N":
        param = benchmark_results.string_length
    else:
        raise ValueError
    stats = pd.concat(
        [
            pd.DataFrame({"parameter": param}),
            benchmark_results[
                ["naive_search", "rabin_karp_search", "knuth_morris_pratt_search"]
            ],
        ],
        axis=1,
    )

    mean_runtime = stats.groupby(by="parameter").mean()[
        ["naive_search", "rabin_karp_search", "knuth_morris_pratt_search"]
    ]
    fig, ax = plt.subplots(1, 3)
    fig.set_size_inches(10, 5)
    fig.suptitle("Complexity by " + parameter)
    for index, algorithm in enumerate(
        ["naive_search", "rabin_karp_search", "knuth_morris_pratt_search"]
    ):
        mean_runtime[algorithm].plot(
            style=".",
            ax=ax[index],
            rot=90,
            xlabel=parameter,
            ylabel="Execution time",
            title=algorithm,
        )
        ax[index].set_xticks([])
        ax[index].set_yticks([])
    plt.show()


def plot_distr_by_substring_ratio(benchmark_results: pd.DataFrame):
    stats = pd.concat(
        [
            pd.DataFrame(
                {
                    "substring_ratio": (benchmark_results.substring_length
                     / benchmark_results.string_length).apply(lambda x: round(x, 1))
                }
            ),
            benchmark_results[
                ["naive_search", "rabin_karp_search", "knuth_morris_pratt_search"]
            ],
        ],
        axis=1,
    )

    mean_runtime = stats.groupby(by="substring_ratio").mean()[
        ["naive_search", "rabin_karp_search", "knuth_morris_pratt_search"]
    ]
    mean_runtime.plot.bar(
        title="Runtime distribution over substring ratio",
        ylabel="Mean execution time (sec)",
        xlabel="Substring search",
    )
    plt.show()

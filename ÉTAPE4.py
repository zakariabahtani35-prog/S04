ca_restaurant = (
    df.groupby('restaurant')['montant_rgl']
      .sum()
      .sort_values(ascending=False)
)

print("\nCA par restaurant:\n", ca_restaurant)

transactions_par_heure = df.groupby('heure')['montant_rgl'].count()

print("\nTransactions par heure:\n", transactions_par_heure)

clients_top = (
    df.groupby('id_client')
      .agg(
          total_depense=('montant_rgl', 'sum'),
          moyenne_transaction=('montant_rgl', 'mean'),
          solde_moyen=('solde_cpp', 'mean')
      )
      .sort_values(by='total_depense', ascending=False)
      .head(10)
)

print("\nTop 10 clients:\n", clients_top)

clients_impayes = (
    df.groupby('id_client')['montant_rst']
      .sum()
      .reset_index()
)

clients_impayes = clients_impayes[clients_impayes['montant_rst'] > 0]

print("\nClients avec impayés:\n", clients_impayes.head())

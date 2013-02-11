% a new version of plotting code, using schemes from colorbrewer2.com

results = csvread( 'results.csv' );

err = results(:,1);

best = err < 0.087;
good = err < 0.95;
mediocre = err < 0.2;
bad = err >= 0.2;

% orange 1
best_color = [ 217/255 71/255 1/255 ];
good_color = [ 253/255 141/255 60/255 ];
mediocre_color = [ 253/255 190/255 133/255 ];
bad_color = [ 254/255 237/255 222/255 ];

% green
best_color = [ 35/255 139/255 69/255 ];
good_color = [ 116/255 196/255 118/255 ];
mediocre_color = [ 186/255 228/255 179/255 ];
bad_color = [ 237/255 248/255 233/255 ];

% orange 2
best_color = [ 204/255 76/255 2/255 ];
good_color = [ 254/255 153/255 41/255 ];
mediocre_color = [ 254/255 217/255 142/255 ];
bad_color = [ 255/255 255/255 212/255 ];


plot( results( bad, 2 ), results( bad, 3 ), 'o', 'Color', bad_color, 'MarkerFaceColor', bad_color )
hold on;

plot( results( mediocre, 2 ), results( mediocre, 3 ), 'o', 'Color', mediocre_color, 'MarkerFaceColor', mediocre_color )
plot( results( good, 2 ), results( good, 3 ), 'o', 'Color', good_color, 'MarkerFaceColor', good_color )
plot( results( best, 2 ), results( best, 3 ), 'o', 'Color', best_color, 'MarkerFaceColor', best_color )

xlabel( 'clusters')
ylabel( 'rbf gamma' )

hold off;


document.addEventListener('DOMContentLoaded', function() {
  const produitPhotoLinks = document.querySelectorAll('.produit-photo');
  const produitDetailButtons = document.querySelectorAll('.produit-detail');
  const produitDetailPopup = document.getElementById('produit-detail-popup');

  produitPhotoLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      const details = JSON.parse(link.dataset.details);
      if (details.photo) {
        produitDetailPopup.innerHTML = `
          <div class="produit-detail-popup">
            <img src="http://boutiquebambino.shop/eshop/productImages/${details.codepro}/${details.photo}" alt="${details.nompro}" />
            <h2>${details.nompro}</h2>
            <p>${details.description}</p>
          </div>
        `;
      } else {
        alert('Détails indisponibles pour ce produit.');
      }
    });
  });

  produitDetailButtons.forEach(button => {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      const details = JSON.parse(button.dataset.details);
      if (details.photo) {
        produitDetailPopup.innerHTML = `
          <div class="produit-detail-popup">
            <img src="http://boutiquebambino.shop/eshop/productImages/${details.codepro}/${details.photo}" alt="${details.nompro}" />
            <h2>${details.nompro}</h2>
            <p>${details.description}</p>
          </div>
        `;
      } else {
        alert('Détails indisponibles pour ce produit.');
      }
    });
  });
});
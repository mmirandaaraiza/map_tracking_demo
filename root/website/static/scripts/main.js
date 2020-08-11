axios.get('/api/vehicles/')
    .then((response) => {
        const vehicles = response.data;

        if (vehicles.length > 0) {
            const mymap = L.map('mapid').setView([vehicles[0].lat, vehicles[0].long], 10);

            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1,
                /** Change the access token in here **/
                accessToken: ''
            }).addTo(mymap);

            vehicles.forEach((vehicle) => {
                L.marker([vehicle.lat, vehicle.long]).addTo(mymap);
            });
        } else {
            const notice = document.createElement('div');
            notice.classList.add('alert', 'alert-danger');
            notice.textContent = 'You have no vehicles to show';

            document.getElementById('mapid').appendChild( notice );
        }
    })
    .catch(function (error) {
        console.log(error);

        const notice = document.createElement('div');
        notice.classList.add('alert', 'alert-danger');
        notice.textContent = 'There was an error trying to get the vehicles';

        document.getElementById('mapid').appendChild( notice );
    });


<script setup>
import {useRoute} from 'vue-router'

const route = useRoute()
const slug = route.params.slug

import {ref, onMounted} from 'vue'
import axios from 'axios'

const apartment = ref(null)
const fetchApartment = async () => {
  const response = await axios.get(`${import.meta.env.VITE_API_URL}/apartments/apartments/${slug}/`)
  apartment.value = response.data
}
onMounted(fetchApartment)
</script>

<template>
  <div v-if="apartment">
    <h1>{{ apartment.name }}</h1>
    <span>{{ apartment.slug }}</span>
    <hr>
    <div class="description">
      <span>Apartment description:</span>
      <p>{{ apartment.description }}</p>
    </div>
    <p>Price: ${{ apartment.price }}</p>
    <p>Rooms: {{ apartment.number_of_rooms }}</p>
    <p>Size: {{ apartment.square }} m²</p>
    <p v-if="apartment.availability">
      <span class="availability">Available</span>
    </p>
    <p v-else>
      <span class="availability">Not available</span>
    </p>
    <p>Owner: {{apartment.owner}}</p>
  </div>
  <div v-else>
    <p>Loading details...</p>
  </div>
</template>
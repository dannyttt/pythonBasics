<template>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h3 class="text-center">Distribution Sign-Up</h3>
            <form @submit.prevent="handleSubmitForm">
                <div id="form-group">
                    <label>Event Detail</label>
                    <!-- here going to be a for loop -->
                </div>
                <div class="form-group">
                    <label>First Name</label>
                    <input type="text" class="form-control" v-model="individual.identity.firstName" required>
                </div>
                <div class="form-group">
                    <label>Last Name</label>
                    <input type="text" class="form-control" v-model="individual.identity.lastName" required>
                </div>

                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="text" class="form-control" v-model="individual.identity.phoneNumber" required>
                </div>
                <div class="form-group">
                    <label>Zip Code</label>
                    <input type="text" class="form-control" v-model="individual.zipCode" required>
                </div>
                <!-- <div id="form-group">
                    <label>Questions</label> <br>
                        <label>How did hear from us</label> <br>
                            <p>Check all that apply</p>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" v-model="individual.question.howDidHearBoutUs.facebook" id="flexCheckDefault">
                                <label class="form-check-label" for="flexCheckDefault">
                                    Facebook
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" v-model="individual.question.howDidHearBoutUs.instagram" id="flexCheckChecked" >
                                <label class="form-check-label" for="flexCheckChecked">
                                    Instagram
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" v-model="individual.question.howDidHearBoutUs.twitter" id="flexCheckChecked" >
                                <label class="form-check-label" for="flexCheckChecked">
                                    Twitter
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" v-model="individual.question.howDidHearBoutUs.wordOfMouth" id="flexCheckChecked" >
                                <label class="form-check-label" for="flexCheckChecked">
                                    Word of Mounth
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" v-model="individual.question.howDidHearBoutUs.kmaz1025fm" id="flexCheckChecked" >
                                <label class="form-check-label" for="flexCheckChecked">
                                    KMAZ 102.5FM
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" v-model="individual.question.howDidHearBoutUs.others" id="flexCheckChecked" >
                                <label class="form-check-label" for="flexCheckChecked">
                                    Others
                                </label> <input type="text">
                            </div>
                            <div class="form-group">
                                <label>Would you like the COVID vaccine on during the distribution</label>
                                <div class="form-check">
                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                <label class="form-check-label" for="flexRadioDefault1">
                                    Yes
                                </label>
                                </div>
                                <div class="form-check">
                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2">
                                <label class="form-check-label" for="flexRadioDefault2">
                                    No
                                </label>
                                </div>
                            </div>
                </div> -->
                <button class="btn btn-danger mt-3">Create</button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                individual: {
                   identity: {
                        firstName: "Jenny",
                        lastName: "Saunders",
                        phoneNumber: "83211122"
                    },
                    zipCode: "77888",
                    eventDetail: {
                        locationName: "BBVA Stadium",
                        event_name: "BBVA Stadium Food Distribution",
                        event_type: "Food Distribution",
                        event_date: "2021-10-06"
                    },
                    question: {
                        howDidHearBoutUs: {
                            facebook: "0",
                            instagram: "0",
                            twitter: "0",
                            wordOfMouth: "0",
                            kmaz1025fm: "0",
                            others: "google"
                        },
                        covidVacCheck: "0",
                        covidVacChoice: "Pfizer",
                        confirmVac: "0",
                        addiSupportiveServces: "1",
                        addtionalSupport: "need",
                        numOfChildrenInHouseHold: "2",
                        age65PlusCheck: "1",
                        venteranCheck: "1",
                        raceCheck: "Asian"
                    }
                }
            }
        },
        methods: {
            handleSubmitForm() {
                // url to post to
                let apiURL = 'http://127.0.0.1:5000/form';
                alert('test')
                    alert(this.individual.identity.firstName)
                axios.post(apiURL, this.individual).then(() => {
                    
                    //chnaging the view to the list
                //   this.$router.push('/view')
                  this.individual = {
                    identity: {
                        firstName: "",
                        lastName: "",
                        phoneNumber: ""
                    },
                    zipCode: "",
                    eventDetail: {
                        locationName: " ",
                        event_name: " ",
                        event_type: " ",
                        event_date: " "
                    },
                    question: {
                        howDidHearBoutUs: {
                            facebook: "",
                            instagram: "",
                            twitter: "",
                            wordOfMouth: "",
                            kmaz1025fm: "",
                            others: ""
                        },
                        covidVacCheck: "",
                        covidVacChoice: "",
                        confirmVac: "",
                        addiSupportiveServces: "",
                        addtionalSupport: "",
                        numOfChildrenInHouseHold: "",
                        age65PlusCheck: "",
                        venteranCheck: "",
                        raceCheck: ""
                    }
                  }
                }).catch(error => {
                    console.log(error)
                });
            }
        }
    }
</script>

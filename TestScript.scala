import io.gatling.core.Predef._
import io.gatling.http.Predef._

class TestScript extends Simulation {
     val httpProtocol = http.baseUrl("https://us-central1-aiplatform.googleapis.com")
     .header(name="Authorization", value="Bearer ya29.c.b0AXv0zTPGZOnznIWdoENsUOM6Gxwp6TG4CLZkgdJtb-rgf23W0_U5136qBmczft_v84WKSIWpay9VOXxOjfACwORCAIO87xFapuUGpA0ELQIKtABPj1RMx4BbEdoJL_xDF-yG7lihizNSaGXu4DAPXBKsy_u7n-YVY59L3XmVMiilawPJgz4ir09eEA4jpzNqeavQslKAXlE")
     val scn = scenario("Get VertexAI OUTPUT").exec(
         http(requestName = "get predictions").post(url="/v1/projects/pritish-vertex-ai/locations/us-central1/endpoints/7832243537113513984:predict")
         .body(RawFileBody(filePath="INPUT.json")).asJson
         .check(status.is(expected=200)))


     setUp(
         scn.inject(atOnceUsers(10)).protocols(httpProtocol)
     )
 
 }
